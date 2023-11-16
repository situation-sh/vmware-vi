# NoDiskFound

This exception is thrown when a virtual machine which has no virtual disks is being upgraded or relaid out using the VirtualMachine.upgradeVirtualHardware or upgradeVmLayout commands. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_disk_found import NoDiskFound

# TODO update the JSON string below
json = "{}"
# create an instance of NoDiskFound from a JSON string
no_disk_found_instance = NoDiskFound.from_json(json)
# print the JSON string representation of the object
print NoDiskFound.to_json()

# convert the object into a dict
no_disk_found_dict = no_disk_found_instance.to_dict()
# create an instance of NoDiskFound from a dict
no_disk_found_form_dict = no_disk_found.from_dict(no_disk_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


