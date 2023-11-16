# PatchInstallFailed

This is a general-purpose fault indicating that some error has occurred regarding a patch install.  Data about the fault is available and is presented as a platform specific string. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolled_back** | **bool** | Whether or not the patch install has been rolled back.  If not, a manual rollback is required.  | 

## Example

```python
from vmware_vi.models.patch_install_failed import PatchInstallFailed

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInstallFailed from a JSON string
patch_install_failed_instance = PatchInstallFailed.from_json(json)
# print the JSON string representation of the object
print PatchInstallFailed.to_json()

# convert the object into a dict
patch_install_failed_dict = patch_install_failed_instance.to_dict()
# create an instance of PatchInstallFailed from a dict
patch_install_failed_form_dict = patch_install_failed.from_dict(patch_install_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


