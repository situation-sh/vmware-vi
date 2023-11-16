# HostIoFilterInfo

Information about an IO Filter installed on a host.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Whether or not the filter is available for use.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_io_filter_info import HostIoFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostIoFilterInfo from a JSON string
host_io_filter_info_instance = HostIoFilterInfo.from_json(json)
# print the JSON string representation of the object
print HostIoFilterInfo.to_json()

# convert the object into a dict
host_io_filter_info_dict = host_io_filter_info_instance.to_dict()
# create an instance of HostIoFilterInfo from a dict
host_io_filter_info_form_dict = host_io_filter_info.from_dict(host_io_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


