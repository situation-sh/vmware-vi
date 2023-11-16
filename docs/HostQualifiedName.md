# HostQualifiedName

This data object describes a qualified name of the host used to identify it in a particular context.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The qualified name.  ***Since:*** vSphere API 7.0.3.0  | 
**type** | **str** | The type of the qualified name.  The list of supported values is specified in *HostQualifiedNameType_enum*.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.host_qualified_name import HostQualifiedName

# TODO update the JSON string below
json = "{}"
# create an instance of HostQualifiedName from a JSON string
host_qualified_name_instance = HostQualifiedName.from_json(json)
# print the JSON string representation of the object
print HostQualifiedName.to_json()

# convert the object into a dict
host_qualified_name_dict = host_qualified_name_instance.to_dict()
# create an instance of HostQualifiedName from a dict
host_qualified_name_form_dict = host_qualified_name.from_dict(host_qualified_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


