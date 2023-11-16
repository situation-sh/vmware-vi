# IndependentDiskVMotionNotSupported

An operation on a powered-on virtual machine requests that the virtual machine's disks be moved without choosing a new home datastore for the virtual machine, but the host does not have that capability.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.independent_disk_v_motion_not_supported import IndependentDiskVMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of IndependentDiskVMotionNotSupported from a JSON string
independent_disk_v_motion_not_supported_instance = IndependentDiskVMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print IndependentDiskVMotionNotSupported.to_json()

# convert the object into a dict
independent_disk_v_motion_not_supported_dict = independent_disk_v_motion_not_supported_instance.to_dict()
# create an instance of IndependentDiskVMotionNotSupported from a dict
independent_disk_v_motion_not_supported_form_dict = independent_disk_v_motion_not_supported.from_dict(independent_disk_v_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


