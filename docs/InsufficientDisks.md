# InsufficientDisks

Fault used to denote an insufficient group of disks for a given operation.  See also *HostVsanSystem.AddDisks_Task*, *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_disks import InsufficientDisks

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientDisks from a JSON string
insufficient_disks_instance = InsufficientDisks.from_json(json)
# print the JSON string representation of the object
print InsufficientDisks.to_json()

# convert the object into a dict
insufficient_disks_dict = insufficient_disks_instance.to_dict()
# create an instance of InsufficientDisks from a dict
insufficient_disks_form_dict = insufficient_disks.from_dict(insufficient_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


