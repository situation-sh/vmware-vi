# CustomizationEvent

Base for customization events.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_location** | **str** | The location of the in-guest customization log which will contain details of the customization operation.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.customization_event import CustomizationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationEvent from a JSON string
customization_event_instance = CustomizationEvent.from_json(json)
# print the JSON string representation of the object
print CustomizationEvent.to_json()

# convert the object into a dict
customization_event_dict = customization_event_instance.to_dict()
# create an instance of CustomizationEvent from a dict
customization_event_form_dict = customization_event.from_dict(customization_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


