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
  A compiler type is a grouping of characteristics unique to a specific program that translates computer code written in one programming language (the source language) into another language (the target language). Typically a program that translates source code from a high-level programming language to a lower-level language (e.g., assembly language, object code, or machine code) to create an executable program. [based on https://en.wikipedia.org/wiki/Compiler]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompilerType extends UcoInherentCharacterizationThing {

  private String compilerInformalDescription;
  private String cpeid;
  private String swid;


}