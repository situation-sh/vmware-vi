# NonHomeRDMVMotionNotSupported

An operation on a powered-on virtual machine requests that an existing Raw Disk Mapping end up in a location other than the new home datastore for the virtual machine, but the host does not have that capability.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of an RDM device for which an unsupported move was requested.  This is not guaranteed to be the only such device.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.non_home_rdmv_motion_not_supported import NonHomeRDMVMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of NonHomeRDMVMotionNotSupported from a JSON string
non_home_rdmv_motion_not_supported_instance = NonHomeRDMVMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print NonHomeRDMVMotionNotSupported.to_json()

# convert the object into a dict
non_home_rdmv_motion_not_supported_dict = non_home_rdmv_motion_not_supported_instance.to_dict()
# create an instance of NonHomeRDMVMotionNotSupported from a dict
non_home_rdmv_motion_not_supported_form_dict = non_home_rdmv_motion_not_supported.from_dict(non_home_rdmv_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


