# AddStandaloneHostRequestType

The parameters of *Folder.AddStandaloneHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | 
**comp_res_spec** | [**ComputeResourceConfigSpec**](ComputeResourceConfigSpec.md) |  | [optional] 
**add_connected** | **bool** | Flag to specify whether or not the host should be connected as soon as it is added. The host will not be added if a connection attempt is made and fails.  | 
**license** | **str** | Provide a licenseKey or licenseKeyType. See *LicenseManager*  | [optional] 

## Example

```python
from vmware_vi.models.add_standalone_host_request_type import AddStandaloneHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddStandaloneHostRequestType from a JSON string
add_standalone_host_request_type_instance = AddStandaloneHostRequestType.from_json(json)
# print the JSON string representation of the object
print AddStandaloneHostRequestType.to_json()

# convert the object into a dict
add_standalone_host_request_type_dict = add_standalone_host_request_type_instance.to_dict()
# create an instance of AddStandaloneHostRequestType from a dict
add_standalone_host_request_type_form_dict = add_standalone_host_request_type.from_dict(add_standalone_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


