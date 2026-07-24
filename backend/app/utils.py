def calculate_seo_score(parsed, response_time):
    score = 100
    recommendations = []

    # Title
    if not parsed["title"]:
        score -= 20
        recommendations.append("Add a page title.")
    else:
        recommendations.append("✓ Page title found.")

    # Meta description
    if not parsed["meta_description"]:
        score -= 20
        recommendations.append("Add a meta description.")
    else:
        recommendations.append("✓ Meta description found.")

    # H1
    if parsed["h1_count"] == 0:
        score -= 20
        recommendations.append("No H1 heading found.")
    elif parsed["h1_count"] > 1:
        score -= 10
        recommendations.append(
            f"Multiple H1 headings detected ({parsed['h1_count']})."
        )
    else:
        recommendations.append("✓ Single H1 heading found.")

    # Images
    if parsed["images_missing_alt"] > 0:
        score -= min(20, parsed["images_missing_alt"] * 5)
        recommendations.append(
            f"{parsed['images_missing_alt']} image(s) missing ALT text."
        )
    else:
        recommendations.append("✓ All images have ALT text.")

    # Response time
    if response_time > 1000:
        score -= 10
        recommendations.append("Page response is slow.")
    else:
        recommendations.append("✓ Good response time.")

    score = max(score, 0)

    return score, recommendations