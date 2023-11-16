# CreateSoftwareAdapterRequestType

The parameters of *HostStorageSystem.CreateSoftwareAdapter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostHbaCreateSpec**](HostHbaCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_software_adapter_request_type import CreateSoftwareAdapterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSoftwareAdapterRequestType from a JSON string
create_software_adapter_request_type_instance = CreateSoftwareAdapterRequestType.from_json(json)
# print the JSON string representation of the object
print CreateSoftwareAdapterRequestType.to_json()

# convert the object into a dict
create_software_adapter_request_type_dict = create_software_adapter_request_type_instance.to_dict()
# create an instance of CreateSoftwareAdapterRequestType from a dict
create_software_adapter_request_type_form_dict = create_software_adapter_request_type.from_dict(create_software_adapter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


