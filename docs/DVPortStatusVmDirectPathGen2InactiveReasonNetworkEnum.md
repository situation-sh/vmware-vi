# DVPortStatusVmDirectPathGen2InactiveReasonNetworkEnum

Set of possible values for *DVPortStatus*.*DVPortStatus.vmDirectPathGen2InactiveReasonNetwork*.  Possible values: - `portNptIncompatibleDvs`: The switch for which this port is defined does not support VMDirectPath Gen 2.      See   *DVSFeatureCapability*.*DVSFeatureCapability.vmDirectPathGen2Supported*. - `portNptNoCompatibleNics`: None of the physical NICs used as uplinks for this port support   VMDirectPath Gen 2.      See also *PhysicalNic.vmDirectPathGen2Supported*. - `portNptNoVirtualFunctionsAvailable`: At least some of the physical NICs used as uplinks for this port   support VMDirectPath Gen 2, but all available network-passthrough   resources are in use by other ports. - `portNptDisabledForPort`: VMDirectPath Gen 2 has been explicitly disabled for this port.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


