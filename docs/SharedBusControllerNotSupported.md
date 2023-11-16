# SharedBusControllerNotSupported

The virtual machine has one or more SCSI controllers that are engaged in bus sharing.  This is an error when migrating a powered-on virtual machine, and can be returned as a subfault of DisallowedMigrationDeviceAttached. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.shared_bus_controller_not_supported import SharedBusControllerNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SharedBusControllerNotSupported from a JSON string
shared_bus_controller_not_supported_instance = SharedBusControllerNotSupported.from_json(json)
# print the JSON string representation of the object
print SharedBusControllerNotSupported.to_json()

# convert the object into a dict
shared_bus_controller_not_supported_dict = shared_bus_controller_not_supported_instance.to_dict()
# create an instance of SharedBusControllerNotSupported from a dict
shared_bus_controller_not_supported_form_dict = shared_bus_controller_not_supported.from_dict(shared_bus_controller_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


