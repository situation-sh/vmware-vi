# VslmVClockInfo

Virtual clock info of VStorageObject catalog.  ***Since:*** vSphere API 6.7.2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_clock_time** | **int** | Virtual clock time of VStorageObject catalog.  It is an epoch or generation ID assigned to each VStorageObject operation on a datastore.  ***Since:*** vSphere API 6.7.2  | 

## Example

```python
from vmware_vi.models.vslm_v_clock_info import VslmVClockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VslmVClockInfo from a JSON string
vslm_v_clock_info_instance = VslmVClockInfo.from_json(json)
# print the JSON string representation of the object
print VslmVClockInfo.to_json()

# convert the object into a dict
vslm_v_clock_info_dict = vslm_v_clock_info_instance.to_dict()
# create an instance of VslmVClockInfo from a dict
vslm_v_clock_info_form_dict = vslm_v_clock_info.from_dict(vslm_v_clock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


