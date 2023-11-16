# AlarmFilterSpec

Alarm Filter used to filter/group alarms.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**List[ManagedEntityStatusEnum]**](ManagedEntityStatusEnum.md) | Status array which could be used to filter alarms according to their triggered state.  If all triggered alarms need to be matched an empty array or ManagedEntity::red and ManagedEntity::yellow could be filled in the array.  ***Since:*** vSphere API 6.7  | [optional] 
**type_entity** | **str** | Use values from *AlarmFilterSpecAlarmTypeByEntity_enum*  ***Since:*** vSphere API 6.7  | [optional] 
**type_trigger** | **str** | Use values from *AlarmFilterSpecAlarmTypeByTrigger_enum*  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.alarm_filter_spec import AlarmFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmFilterSpec from a JSON string
alarm_filter_spec_instance = AlarmFilterSpec.from_json(json)
# print the JSON string representation of the object
print AlarmFilterSpec.to_json()

# convert the object into a dict
alarm_filter_spec_dict = alarm_filter_spec_instance.to_dict()
# create an instance of AlarmFilterSpec from a dict
alarm_filter_spec_form_dict = alarm_filter_spec.from_dict(alarm_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


