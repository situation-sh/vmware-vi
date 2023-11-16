# IoFilterInfo

Information about an IO Filter.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | IO Filter identifier.  ***Since:*** vSphere API 6.0  | 
**name** | **str** | Name of the IO Filter.  ***Since:*** vSphere API 6.0  | 
**vendor** | **str** | Vendor of the IO Filter.  ***Since:*** vSphere API 6.0  | 
**version** | **str** | Version of the IO Filter.  ***Since:*** vSphere API 6.0  | 
**type** | **str** | Type of the IO Filter.  The set of possible values are listed in *IoFilterType_enum*. The property is unset if the information is not available.  ***Since:*** vSphere API 6.5  | [optional] 
**summary** | **str** | Short description of the IO Filter.  The property is unset if the information is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**release_date** | **str** | Release date of the IO Filter.  The property is unset if the information is not available.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.io_filter_info import IoFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IoFilterInfo from a JSON string
io_filter_info_instance = IoFilterInfo.from_json(json)
# print the JSON string representation of the object
print IoFilterInfo.to_json()

# convert the object into a dict
io_filter_info_dict = io_filter_info_instance.to_dict()
# create an instance of IoFilterInfo from a dict
io_filter_info_form_dict = io_filter_info.from_dict(io_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


