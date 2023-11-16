# HostMultipathInfoPath

The *HostMultipathInfoPath* data object is a storage entity that represents a topological path from a host bus adapter to a SCSI logical unit.  Each path is unique although each host bus adapter/SCSI logical unit pair can have multiple paths.  Path objects are identified by a key. The specifics of how the key is formatted are dependent on the implementation. Example implementations include using strings like \"vmhba1:0:0:0\". 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Identifier of the path.  | 
**name** | **str** | Name of path.  Use this name to configure LogicalUnit multipathing policy using *HostStorageSystem.EnableMultipathPath* and *HostStorageSystem.DisableMultipathPath*.  | 
**path_state** | **str** | Deprecated as of VI API 4.0: - System reported path states are available in *HostMultipathInfoPath.state*. - Paths slated for I/O can be found using *HostMultipathInfoPath.isWorkingPath*.  State of the path.  Must be one of the values of *MultipathState_enum* &lt;dl&gt; &lt;dt&gt;active&lt;/dt&gt; &lt;dd&gt;Path can be used for I/O and is currently a working path.&lt;/dd&gt; &lt;dt&gt;standby&lt;/dt&gt; &lt;dd&gt;Path can be used for I/O but is not a working path or can be used if active paths fail.&lt;/dd&gt; &lt;dt&gt;disabled&lt;/dt&gt; &lt;dd&gt;Path has been administratively disabled.&lt;/dd&gt; &lt;dt&gt;dead&lt;/dt&gt; &lt;dd&gt;Path cannot be used for I/O.&lt;/dd&gt; &lt;dt&gt;unknown&lt;/dt&gt; &lt;dd&gt;Path is in unknown error state.&lt;/dd&gt; &lt;/dl&gt;  | 
**state** | **str** | System-reported state of the path.  Must be one of the values of *MultipathState_enum* &lt;dl&gt; &lt;dt&gt;active&lt;/dt&gt; &lt;dd&gt;Path can be used for I/O.&lt;/dd&gt; &lt;dt&gt;standby&lt;/dt&gt; &lt;dd&gt;Path can be used for I/O if active paths fail.&lt;/dd&gt; &lt;dt&gt;disabled&lt;/dt&gt; &lt;dd&gt;Path has been administratively disabled.&lt;/dd&gt; &lt;dt&gt;dead&lt;/dt&gt; &lt;dd&gt;Path cannot be used for I/O.&lt;/dd&gt; &lt;dt&gt;unknown&lt;/dt&gt; &lt;dd&gt;Path is in unknown error state.&lt;/dd&gt; &lt;/dl&gt;  ***Since:*** vSphere API 4.0  | [optional] 
**is_working_path** | **bool** | A path, managed by a given path selection policy(psp) plugin, is denoted to be a Working Path if the psp plugin is likely to select the path for performing I/O in the near future.  ***Since:*** vSphere API 4.0  | [optional] 
**adapter** | [**HostHostBusAdapter**](HostHostBusAdapter.md) |  | 
**lun** | [**HostMultipathInfoLogicalUnit**](HostMultipathInfoLogicalUnit.md) |  | 
**transport** | [**HostTargetTransport**](HostTargetTransport.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_multipath_info_path import HostMultipathInfoPath

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoPath from a JSON string
host_multipath_info_path_instance = HostMultipathInfoPath.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoPath.to_json()

# convert the object into a dict
host_multipath_info_path_dict = host_multipath_info_path_instance.to_dict()
# create an instance of HostMultipathInfoPath from a dict
host_multipath_info_path_form_dict = host_multipath_info_path.from_dict(host_multipath_info_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


