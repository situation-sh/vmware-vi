# RestoreFirmwareConfigurationRequestType

The parameters of *HostFirmwareSystem.RestoreFirmwareConfiguration*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Forces application of the configuration even if the bundle is mismatched.  | 

## Example

```python
from vmware_vi.models.restore_firmware_configuration_request_type import RestoreFirmwareConfigurationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreFirmwareConfigurationRequestType from a JSON string
restore_firmware_configuration_request_type_instance = RestoreFirmwareConfigurationRequestType.from_json(json)
# print the JSON string representation of the object
print RestoreFirmwareConfigurationRequestType.to_json()

# convert the object into a dict
restore_firmware_configuration_request_type_dict = restore_firmware_configuration_request_type_instance.to_dict()
# create an instance of RestoreFirmwareConfigurationRequestType from a dict
restore_firmware_configuration_request_type_form_dict = restore_firmware_configuration_request_type.from_dict(restore_firmware_configuration_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


