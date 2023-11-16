# HostDateTimeSystemTimeZone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the time zone.  ***Since:*** VI API 2.5  | 
**name** | **str** | The time zone name.  ***Since:*** VI API 2.5  | 
**description** | **str** | Description of the time zone.  ***Since:*** VI API 2.5  | 
**gmt_offset** | **int** | The GMT offset in seconds that is currently applicable to the timezone (with respect to the current time on the host).  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_date_time_system_time_zone import HostDateTimeSystemTimeZone

# TODO update the JSON string below
json = "{}"
# create an instance of HostDateTimeSystemTimeZone from a JSON string
host_date_time_system_time_zone_instance = HostDateTimeSystemTimeZone.from_json(json)
# print the JSON string representation of the object
print HostDateTimeSystemTimeZone.to_json()

# convert the object into a dict
host_date_time_system_time_zone_dict = host_date_time_system_time_zone_instance.to_dict()
# create an instance of HostDateTimeSystemTimeZone from a dict
host_date_time_system_time_zone_form_dict = host_date_time_system_time_zone.from_dict(host_date_time_system_time_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


