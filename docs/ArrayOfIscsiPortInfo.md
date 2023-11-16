# ArrayOfIscsiPortInfo

A boxed array of *IscsiPortInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiPortInfo]**](IscsiPortInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_port_info import ArrayOfIscsiPortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiPortInfo from a JSON string
array_of_iscsi_port_info_instance = ArrayOfIscsiPortInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiPortInfo.to_json()

# convert the object into a dict
array_of_iscsi_port_info_dict = array_of_iscsi_port_info_instance.to_dict()
# create an instance of ArrayOfIscsiPortInfo from a dict
array_of_iscsi_port_info_form_dict = array_of_iscsi_port_info.from_dict(array_of_iscsi_port_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


