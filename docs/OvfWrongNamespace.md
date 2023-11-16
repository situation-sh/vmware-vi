# OvfWrongNamespace

A OvfWrongNamespace exception is throw if the ovf descriptor has a Namespace error as defined in the Ovf spec  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | The name of the invalid namespace  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_wrong_namespace import OvfWrongNamespace

# TODO update the JSON string below
json = "{}"
# create an instance of OvfWrongNamespace from a JSON string
ovf_wrong_namespace_instance = OvfWrongNamespace.from_json(json)
# print the JSON string representation of the object
print OvfWrongNamespace.to_json()

# convert the object into a dict
ovf_wrong_namespace_dict = ovf_wrong_namespace_instance.to_dict()
# create an instance of OvfWrongNamespace from a dict
ovf_wrong_namespace_form_dict = ovf_wrong_namespace.from_dict(ovf_wrong_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


