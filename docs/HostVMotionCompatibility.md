# HostVMotionCompatibility

The object type for the array returned by queryVMotionCompatibility; specifies the VMotion compatibility types for a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**compatibility** | **List[str]** | Ways in which the host is compatible with the designated virtual machine that is a candidate for VMotion.  This array will be a subset of the set of VMotionCompatibilityType strings that were input to queryVMotionCompatibility.  | [optional] 

## Example

```python
from vmware_vi.models.host_v_motion_compatibility import HostVMotionCompatibility

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionCompatibility from a JSON string
host_v_motion_compatibility_instance = HostVMotionCompatibility.from_json(json)
# print the JSON string representation of the object
print HostVMotionCompatibility.to_json()

# convert the object into a dict
host_v_motion_compatibility_dict = host_v_motion_compatibility_instance.to_dict()
# create an instance of HostVMotionCompatibility from a dict
host_v_motion_compatibility_form_dict = host_v_motion_compatibility.from_dict(host_v_motion_compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


