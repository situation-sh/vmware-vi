# NamespaceWriteProtected

A NamespaceWriteProtected fault is thrown when an operation on namespace fails because namespace is write-protected.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The namespace in question.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.namespace_write_protected import NamespaceWriteProtected

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceWriteProtected from a JSON string
namespace_write_protected_instance = NamespaceWriteProtected.from_json(json)
# print the JSON string representation of the object
print NamespaceWriteProtected.to_json()

# convert the object into a dict
namespace_write_protected_dict = namespace_write_protected_instance.to_dict()
# create an instance of NamespaceWriteProtected from a dict
namespace_write_protected_form_dict = namespace_write_protected.from_dict(namespace_write_protected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


