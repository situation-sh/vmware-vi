# UnsharedSwapVMotionNotSupported

The compute resource and virtual machine configurations for swapfile placement would require the virtual machine swapfile to change location for this VMotion; however the host does not support this.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.unshared_swap_v_motion_not_supported import UnsharedSwapVMotionNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of UnsharedSwapVMotionNotSupported from a JSON string
unshared_swap_v_motion_not_supported_instance = UnsharedSwapVMotionNotSupported.from_json(json)
# print the JSON string representation of the object
print UnsharedSwapVMotionNotSupported.to_json()

# convert the object into a dict
unshared_swap_v_motion_not_supported_dict = unshared_swap_v_motion_not_supported_instance.to_dict()
# create an instance of UnsharedSwapVMotionNotSupported from a dict
unshared_swap_v_motion_not_supported_form_dict = unshared_swap_v_motion_not_supported.from_dict(unshared_swap_v_motion_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


