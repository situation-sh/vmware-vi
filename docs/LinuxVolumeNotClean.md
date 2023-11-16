# LinuxVolumeNotClean

Customization operation is performed on a linux source vm that was not shut down properly.  If the filesystem has significant fsck errors on it, customization process cannot make changes to it. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.linux_volume_not_clean import LinuxVolumeNotClean

# TODO update the JSON string below
json = "{}"
# create an instance of LinuxVolumeNotClean from a JSON string
linux_volume_not_clean_instance = LinuxVolumeNotClean.from_json(json)
# print the JSON string representation of the object
print LinuxVolumeNotClean.to_json()

# convert the object into a dict
linux_volume_not_clean_dict = linux_volume_not_clean_instance.to_dict()
# create an instance of LinuxVolumeNotClean from a dict
linux_volume_not_clean_form_dict = linux_volume_not_clean.from_dict(linux_volume_not_clean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


