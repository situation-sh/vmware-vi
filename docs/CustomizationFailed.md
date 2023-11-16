# CustomizationFailed

The customization sequence in the guest failed.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason why the customization failed @see CustomizationFailed.ReasonCode .  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.customization_failed import CustomizationFailed

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationFailed from a JSON string
customization_failed_instance = CustomizationFailed.from_json(json)
# print the JSON string representation of the object
print CustomizationFailed.to_json()

# convert the object into a dict
customization_failed_dict = customization_failed_instance.to_dict()
# create an instance of CustomizationFailed from a dict
customization_failed_form_dict = customization_failed.from_dict(customization_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


