# ConfigureEvcModeRequestType

The parameters of *ClusterEVCManager.ConfigureEvcMode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evc_mode_key** | **str** | A key referencing the desired EVC mode.  | 
**evc_graphics_mode_key** | **str** | A key referencing the desired EVC Graphics mode *Capability.supportedEVCGraphicsMode*.  | [optional] 

## Example

```python
from vmware_vi.models.configure_evc_mode_request_type import ConfigureEvcModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureEvcModeRequestType from a JSON string
configure_evc_mode_request_type_instance = ConfigureEvcModeRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureEvcModeRequestType.to_json()

# convert the object into a dict
configure_evc_mode_request_type_dict = configure_evc_mode_request_type_instance.to_dict()
# create an instance of ConfigureEvcModeRequestType from a dict
configure_evc_mode_request_type_form_dict = configure_evc_mode_request_type.from_dict(configure_evc_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


