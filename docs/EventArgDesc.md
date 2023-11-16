# EventArgDesc

Describes an available event argument name for an Event type, which can be used in *EventAlarmExpression*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the argument  ***Since:*** vSphere API 4.0  | 
**type** | **str** | The type of the argument.  ***Since:*** vSphere API 4.0  | 
**description** | [**ElementDescription**](ElementDescription.md) |  | [optional] 

## Example

```python
from vmware_vi.models.event_arg_desc import EventArgDesc

# TODO update the JSON string below
json = "{}"
# create an instance of EventArgDesc from a JSON string
event_arg_desc_instance = EventArgDesc.from_json(json)
# print the JSON string representation of the object
print EventArgDesc.to_json()

# convert the object into a dict
event_arg_desc_dict = event_arg_desc_instance.to_dict()
# create an instance of EventArgDesc from a dict
event_arg_desc_form_dict = event_arg_desc.from_dict(event_arg_desc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


