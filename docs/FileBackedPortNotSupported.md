# FileBackedPortNotSupported

The virtual machine has a port (either a SerialPort or a ParallelPort) which is backed by a file.  This is an error when migrating a virtual machine with the device connected, and can be returned as a subfault of DisallowedMigrationDeviceAttached.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.file_backed_port_not_supported import FileBackedPortNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of FileBackedPortNotSupported from a JSON string
file_backed_port_not_supported_instance = FileBackedPortNotSupported.from_json(json)
# print the JSON string representation of the object
print FileBackedPortNotSupported.to_json()

# convert the object into a dict
file_backed_port_not_supported_dict = file_backed_port_not_supported_instance.to_dict()
# create an instance of FileBackedPortNotSupported from a dict
file_backed_port_not_supported_form_dict = file_backed_port_not_supported.from_dict(file_backed_port_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


