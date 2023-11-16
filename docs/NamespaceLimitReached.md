# NamespaceLimitReached

A NamespaceLimitReached fault is thrown when the maximum allowed namespaces for a virtual machine will be exceeded.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Allowed maximum number of namespaces per virtual machine.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.namespace_limit_reached import NamespaceLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceLimitReached from a JSON string
namespace_limit_reached_instance = NamespaceLimitReached.from_json(json)
# print the JSON string representation of the object
print NamespaceLimitReached.to_json()

# convert the object into a dict
namespace_limit_reached_dict = namespace_limit_reached_instance.to_dict()
# create an instance of NamespaceLimitReached from a dict
namespace_limit_reached_form_dict = namespace_limit_reached.from_dict(namespace_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


