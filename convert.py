from mdcv import markdown_to_html, load_config


config = load_config()
markdown_to_html("README.md", 'index.html', config=config)