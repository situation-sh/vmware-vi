# CustomizationPending

A customization operation is already pending on this virtual machine and is awaiting power-up to complete.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_pending import CustomizationPending

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationPending from a JSON string
customization_pending_instance = CustomizationPending.from_json(json)
# print the JSON string representation of the object
print CustomizationPending.to_json()

# convert the object into a dict
customization_pending_dict = customization_pending_instance.to_dict()
# create an instance of CustomizationPending from a dict
customization_pending_form_dict = customization_pending.from_dict(customization_pending_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


