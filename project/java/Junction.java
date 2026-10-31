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
  A junction is a specific NTFS (New Technology File System) reparse point to redirect a directory access to another directory which can be on the same volume or another volume. A junction is similar to a directory symbolic link but may differ on whether they are processed on the local system or on the remote file server. [based on https://jp-andre.pagesperso-orange.fr/junctions.html]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Junction extends FileSystemObject {



}