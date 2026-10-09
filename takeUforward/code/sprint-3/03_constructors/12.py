# Mixin Classes with Constructor Chaining
# Mixins provide composable, reusable behavior across unrelated classes.
# Implement two mixins and chain their constructors cooperatively:
#
# 1. AuditMixin:
#    - In __init__, extract `created_by` (default "system") and store as self.created_by.
#    - Forward remaining arguments to super().__init__(*args, **kwargs).
#
# 2. TagMixin:
#    - In __init__, extract `tags` (default None -> empty list) and store as self.tags.
#    - Forward remaining arguments to super().__init__(*args, **kwargs).
#
# 3. Document(AuditMixin, TagMixin):
#    - In __init__(self, title, content, **kwargs):
#      store self.title = title, self.content = content.
#      Forward kwargs to super().__init__(**kwargs).
#
# Example:
# Input:
#   doc = Document(title="SRS", content="Specs...", created_by="Raj", tags=["v1", "draft"])
# Output:
#   doc.title == "SRS"
#   doc.content == "Specs..."
#   doc.created_by == "Raj"
#   doc.tags == ["v1", "draft"]
#

# Write your solution below:

class AuditMixin : 
    def __init__(self , created_by = "system" , **kwargs) :
        self.created_by = created_by 
        super().__init__(**kwargs)

class TagMixin : 
    def __init__(self , tags = None , **kwargs) :
        self.tags = tags or [] 
        super().__init__(**kwargs)

class Document(AuditMixin , TagMixin) : 
    def __init__(self , title , content , **kwargs) :
        self.title = title 
        self.content = content 
        super().__init__(**kwargs)

doc = Document(title="SRS", content="Specs...", created_by="Raj", tags=["v1", "draft"])
print(doc.title, doc.content, doc.created_by, doc.tags)

