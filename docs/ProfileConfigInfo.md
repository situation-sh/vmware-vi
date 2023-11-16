# ProfileConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the profile  ***Since:*** vSphere API 4.0  | 
**annotation** | **str** | User Provided description of the profile  ***Since:*** vSphere API 4.0  | [optional] 
**enabled** | **bool** | Flag indicating if the Profile is enabled  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_config_info import ProfileConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileConfigInfo from a JSON string
profile_config_info_instance = ProfileConfigInfo.from_json(json)
# print the JSON string representation of the object
print ProfileConfigInfo.to_json()

# convert the object into a dict
profile_config_info_dict = profile_config_info_instance.to_dict()
# create an instance of ProfileConfigInfo from a dict
profile_config_info_form_dict = profile_config_info.from_dict(profile_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


