# ReplicationVmConfigFaultReasonForFaultEnum

Possible values: - `incompatibleHwVersion`: Incompatible VM hardware version - `invalidVmReplicationId`: Invalid VM Replication ID string - `invalidGenerationNumber`: Invalid generation number in VM's configuration - `outOfBoundsRpoValue`: Invalid RPO value (out of bounds) - `invalidDestinationIpAddress`: Invalid destination IP address - `invalidDestinationPort`: Invalid destination port - `invalidExtraVmOptions`: Malformed extra options list - `staleGenerationNumber`: Mis-matching generation number (stale) - `reconfigureVmReplicationIdNotAllowed`: Attempting to re-configure the VM replication ID - `cannotRetrieveVmReplicationConfiguration`: Could not retrieve the VM configuration - `replicationAlreadyEnabled`: Attempting to re-enable replication for the VM - `invalidPriorConfiguration`: The existing replication configuration of the VM is broken   (applicable to re-configuration only). - `replicationNotEnabled`: Attempting to re-configure or disable replication for a VM   for which replication has not been enabled. - `replicationConfigurationFailed`: Failed to commit the new replication properties for the VM. - `encryptedVm`: VM is encrypted      ***Since:*** vSphere API 6.5 - `invalidThumbprint`: Remote certificate thumbprint is invalid      ***Since:*** vSphere API 6.7 - `incompatibleDevice`: VM hardware contains devices incompatible with replication      ***Since:*** vSphere API 6.7  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


