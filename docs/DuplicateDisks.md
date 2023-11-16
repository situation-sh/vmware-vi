# DuplicateDisks

Fault used to denote a duplicate set of disks were incorrectly specified for a given operation.  See also *HostVsanSystem.AddDisks_Task*, *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.duplicate_disks import DuplicateDisks

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateDisks from a JSON string
duplicate_disks_instance = DuplicateDisks.from_json(json)
# print the JSON string representation of the object
print DuplicateDisks.to_json()

# convert the object into a dict
duplicate_disks_dict = duplicate_disks_instance.to_dict()
# create an instance of DuplicateDisks from a dict
duplicate_disks_form_dict = duplicate_disks.from_dict(duplicate_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


