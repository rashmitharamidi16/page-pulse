from app.parser import parse_html


def test_parse_html():
    html = """
    <html>
        <head>
            <title>Test Page</title>
            <meta name="description" content="Test Description">
        </head>
        <body>
            <h1>Hello</h1>
            <h1>World</h1>

            <img src="one.jpg">
            <img src="two.jpg" alt="Image">

            <p>This is a sample paragraph.</p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["title"] == "Test Page"
    assert result["meta_description"] == "Test Description"
    assert result["h1_count"] == 2
    assert result["images_missing_alt"] == 1
    assert result["word_count"] > 0