# HostPatchManagerLocator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL that will be used to access the patch repository.  | 
**proxy** | **str** | The proxy setting required to access the URL from the host.  If unset, a direct URL connection will be attempted.  | [optional] 

## Example

```python
from vmware_vi.models.host_patch_manager_locator import HostPatchManagerLocator

# TODO update the JSON string below
json = "{}"
# create an instance of HostPatchManagerLocator from a JSON string
host_patch_manager_locator_instance = HostPatchManagerLocator.from_json(json)
# print the JSON string representation of the object
print HostPatchManagerLocator.to_json()

# convert the object into a dict
host_patch_manager_locator_dict = host_patch_manager_locator_instance.to_dict()
# create an instance of HostPatchManagerLocator from a dict
host_patch_manager_locator_form_dict = host_patch_manager_locator.from_dict(host_patch_manager_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


