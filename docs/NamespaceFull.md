# NamespaceFull

A NamespaceFull fault is thrown when an operation on namespace requires more space to complete.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The namespace in question.  ***Since:*** vSphere API 5.1  | 
**current_max_size** | **int** | Current maximum size.  ***Since:*** vSphere API 5.1  | 
**required_size** | **int** | Size necessary to complete operation.  If not present, system was not able to determine how much space would be necessary to complete operation.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.namespace_full import NamespaceFull

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceFull from a JSON string
namespace_full_instance = NamespaceFull.from_json(json)
# print the JSON string representation of the object
print NamespaceFull.to_json()

# convert the object into a dict
namespace_full_dict = namespace_full_instance.to_dict()
# create an instance of NamespaceFull from a dict
namespace_full_form_dict = namespace_full.from_dict(namespace_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


