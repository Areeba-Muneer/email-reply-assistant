class ValidationError(ValueError): pass

def validate_reply(reply):
    if not isinstance(reply,str) or not reply.strip(): raise ValidationError("Reply is empty.")
    if len(reply)<10: raise ValidationError("Reply is too short.")
    if len(reply)>6000: raise ValidationError("Reply is too long. Try again with a shorter email.")
    if any(x in reply.lower() for x in ["[insert","[your name]","[recipient name]","<your name>"]):
        raise ValidationError("Reply contains a placeholder. Review it before use.")
