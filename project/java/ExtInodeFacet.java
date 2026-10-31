package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An extInode facet is a grouping of characteristics unique to a file system object (file, directory, etc.) conformant to the extended file system (EXT or related derivations) specification.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExtInodeFacet extends Facet {

  private ZonedDateTime extDeletionTime;
  private Integer extFileType;
  private Integer extFlags;
  private Integer extHardLinkCount;
  private ZonedDateTime extInodeChangeTime;
  private Integer extInodeID;
  private Integer extPermissions;
  private Integer extSGID;
  private Integer extSUID;


}