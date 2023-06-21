from jinja2 import Environment, PackageLoader


def render_report():
    # Create a Jinja2 environment
    env = Environment(loader=PackageLoader('pycrostates_report','report/templates'))
    # Define data to be passed to the template
    data = {
        'title': 'My Webpage',
        'sections': [
            {'id': 'gev', 'title': 'GEV Section'},
            {'id': 'embedding', 'title': 'Embedding Section'},
            {'id': 'correlation', 'title': 'Correlation Section'},
            {'id': 'method', 'title': 'Method Section'}
        ]
    }
    # Render the template
    template = env.get_template('report.jinja')
    output = template.render(data)
    return output

