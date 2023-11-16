# NoPermissionOnNasVolume

This fault is thrown when an operation to configure a NAS volume fails because of insufficient user permissions.  For CIFS volumes, this implies that the user specified in the *spec* does not have access to the network resource.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.no_permission_on_nas_volume import NoPermissionOnNasVolume

# TODO update the JSON string below
json = "{}"
# create an instance of NoPermissionOnNasVolume from a JSON string
no_permission_on_nas_volume_instance = NoPermissionOnNasVolume.from_json(json)
# print the JSON string representation of the object
print NoPermissionOnNasVolume.to_json()

# convert the object into a dict
no_permission_on_nas_volume_dict = no_permission_on_nas_volume_instance.to_dict()
# create an instance of NoPermissionOnNasVolume from a dict
no_permission_on_nas_volume_form_dict = no_permission_on_nas_volume.from_dict(no_permission_on_nas_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


