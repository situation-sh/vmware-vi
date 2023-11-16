# HostImageProfileSummary

Summary of an image profile  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the image profile  ***Since:*** vSphere API 5.0  | 
**vendor** | **str** | The organization publishing the image profile.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_image_profile_summary import HostImageProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HostImageProfileSummary from a JSON string
host_image_profile_summary_instance = HostImageProfileSummary.from_json(json)
# print the JSON string representation of the object
print HostImageProfileSummary.to_json()

# convert the object into a dict
host_image_profile_summary_dict = host_image_profile_summary_instance.to_dict()
# create an instance of HostImageProfileSummary from a dict
host_image_profile_summary_form_dict = host_image_profile_summary.from_dict(host_image_profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


