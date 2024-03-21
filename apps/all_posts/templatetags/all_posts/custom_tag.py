from django import template

register = template.Library()


@register.simple_tag
def render_replies(comments):
    """Renders replies with unlimited nesting."""
    html = ""
    for comment in comments:
        html += """
    <div class="comment">
      <p><b>{{ comment.username }}</b> - {{ comment.pubDate }}</p>
      <p>{{ comment.text }}</p>
      <div class="replies">
        {{ render_replies comments=comment.child_comments }}
      </div>
    </div>
    """
    return html
