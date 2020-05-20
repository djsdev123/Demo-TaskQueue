from flask import Flask, url_for, jsonify
from celery_worker.celery_task import reverse


app = Flask(__name__)


@app.route('/process/<string:name>')
def process(name):
    #reverse.delay(name)
    task = reverse.apply_async(queue='high_priority', args=(name,))
    header = {
        'Location': url_for('taskstatus', task_id=task.id)
    }
    return jsonify({}), 202, header


@app.route('/status/<string:task_id>')
def taskstatus(task_id):
    task = reverse.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'status': 'pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'status': task.status
        }
        task_infos = task.__dict__
        if task_infos['_cache'] is not None:
            response['reslut'] = task_infos['_cache'].get('result')
    else:
        response = {
            'state': task.state,
            'status': str(task.info)
        }
    return jsonify(response)
        



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)