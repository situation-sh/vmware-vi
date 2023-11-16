# CustomizationSysprepFailed

Sysprep failed to run in the guest during customization.  This will most like have been caused by the fact that the wrong sysprep was used for the guest, so we include the version information in the event.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sysprep_version** | **str** | The version string for the sysprep files that were included in the customization package.  ***Since:*** VI API 2.5  | 
**system_version** | **str** | The version string for the system  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.customization_sysprep_failed import CustomizationSysprepFailed

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSysprepFailed from a JSON string
customization_sysprep_failed_instance = CustomizationSysprepFailed.from_json(json)
# print the JSON string representation of the object
print CustomizationSysprepFailed.to_json()

# convert the object into a dict
customization_sysprep_failed_dict = customization_sysprep_failed_instance.to_dict()
# create an instance of CustomizationSysprepFailed from a dict
customization_sysprep_failed_form_dict = customization_sysprep_failed.from_dict(customization_sysprep_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


