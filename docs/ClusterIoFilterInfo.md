# ClusterIoFilterInfo

Information about an IO Filter on a compute resource.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_type** | **str** | The operation that was performed for the IO Filter.  The set of possible values are described in *IoFilterOperation_enum*. If opType is *uninstall*, and the uninstallation of the filter was sucessful on all the hosts in the cluster, the filter will be removed from the cluster&#39;s filter list.  ***Since:*** vSphere API 6.0  | 
**vib_url** | **str** | The URL of the VIB package that the IO Filter is installed from.  The property is unset if the information is not available.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_io_filter_info import ClusterIoFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIoFilterInfo from a JSON string
cluster_io_filter_info_instance = ClusterIoFilterInfo.from_json(json)
# print the JSON string representation of the object
print ClusterIoFilterInfo.to_json()

# convert the object into a dict
cluster_io_filter_info_dict = cluster_io_filter_info_instance.to_dict()
# create an instance of ClusterIoFilterInfo from a dict
cluster_io_filter_info_form_dict = cluster_io_filter_info.from_dict(cluster_io_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


