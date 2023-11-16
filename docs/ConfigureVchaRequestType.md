# ConfigureVchaRequestType

The parameters of *FailoverClusterConfigurator.configureVcha_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**VchaClusterConfigSpec**](VchaClusterConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.configure_vcha_request_type import ConfigureVchaRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureVchaRequestType from a JSON string
configure_vcha_request_type_instance = ConfigureVchaRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureVchaRequestType.to_json()

# convert the object into a dict
configure_vcha_request_type_dict = configure_vcha_request_type_instance.to_dict()
# create an instance of ConfigureVchaRequestType from a dict
configure_vcha_request_type_form_dict = configure_vcha_request_type.from_dict(configure_vcha_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


