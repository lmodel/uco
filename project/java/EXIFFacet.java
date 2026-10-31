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
  An EXIF (exchangeable image file format) facet is a grouping of characteristics unique to the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras conformant to JEIDA/JEITA/CIPA specifications. [based on https://en.wikipedia.org/wiki/Exif]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EXIFFacet extends Facet {

  private List<ControlledDictionary> exifData;


}