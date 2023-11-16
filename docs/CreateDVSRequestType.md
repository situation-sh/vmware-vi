# CreateDVSRequestType

The parameters of *Folder.CreateDVS_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**DVSCreateSpec**](DVSCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_dvs_request_type import CreateDVSRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDVSRequestType from a JSON string
create_dvs_request_type_instance = CreateDVSRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDVSRequestType.to_json()

# convert the object into a dict
create_dvs_request_type_dict = create_dvs_request_type_instance.to_dict()
# create an instance of CreateDVSRequestType from a dict
create_dvs_request_type_form_dict = create_dvs_request_type.from_dict(create_dvs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


